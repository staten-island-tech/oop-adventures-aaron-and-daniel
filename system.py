def run_trivia_game():
    def reset_game():
        nonlocal current_question, score, streak, highest_streak, game_over, power_up_used
        current_question = 0
        score = 0
        streak = 0
        power_up_used = False
        game_over = False
        random.shuffle(questions)
        for question in questions:
            random.shuffle(question.options)

    current_question = 0
    score = 0
    streak = 0
    power_up_used = False
    highest_streak = load_highest_streak()  
    game_over = False
    
    random.shuffle(questions)
    for question in questions:
        random.shuffle(question.options)
    
    while True:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_over:
            game_over_text = large_font.render("Game Over!", True, WHITE)
            score_text = font.render(f"Your Score: {score}/{len(questions)}", True, WHITE)
            streak_text = font.render(f"Current Streak: {streak}", True, WHITE)
            highest_streak_text = font.render(f"Highest Streak: {highest_streak}", True, WHITE)

            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
            screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2))
            screen.blit(streak_text, (20, 20)) 
            screen.blit(highest_streak_text, (screen_width - highest_streak_text.get_width() - 20, 20))  
            
            play_again_button = Button(screen_width // 2 - 100, screen_height // 1.5, 200, 50, BLUE, "Play Again")
            play_again_button.draw(screen)

            pygame.display.flip()

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_again_button.is_clicked(mouse_pos, mouse_pressed):
                if streak > highest_streak:
                    highest_streak = streak
                    save_highest_streak(highest_streak)  
                reset_game()  

        else:
            question = questions[current_question]
            question_text = font.render(question.question, True, WHITE)
            screen.blit(question_text, (205, 100))